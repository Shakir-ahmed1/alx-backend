import redis from 'redis';

const publisher = redis.createClient();
const channel = 'holberton school channel';



function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(channel, message);
}, time);

}
publishMessage("Holberton Student #1 starts course", 1000);
publishMessage("Holberton Student #2 starts course", 2000);
publishMessage("KILL_SERVER", 3000);
publishMessage("Holberton Student #3 starts course", 4000)
