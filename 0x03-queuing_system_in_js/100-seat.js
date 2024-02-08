const express = require('express');
const kue = require('kue');
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const queue = kue.createQueue();

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats) : 0;
};

reserveSeat(50);
let reservationEnabled = true;

const app = express();
const PORT = 1245;

// routes
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
  } else {
    const job = queue.create('reserve_seat').save((err) => {
      if (err) {
        res.json({ status: 'Reservation failed' });
      } else {
        res.json({ status: 'Reservation in process' });
      }
    });
  }
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeats();
  await reserveSeat(currentAvailableSeats - 1);

  if (currentAvailableSeats - 1 === 0) {
    reservationEnabled = false;
  }
});

queue.process('reserve_seat', async (job, done) => {
  const currentAvailableSeats = await getCurrentAvailableSeats();

  if (currentAvailableSeats <= 0) {
    done(new Error('Not enough seats available'));
  } else {
    done();
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

