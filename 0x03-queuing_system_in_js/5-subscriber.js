import redis from 'redis';

const subscriber = redis.createClient();
const channel = 'holberton school channel';
subscriber.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
subscriber.on('connect', () => console.log('Redis client connected to the server'));

subscriber.subscribe(channel);

subscriber.on('message', (chann, message) => {
  if (chann === channel) {
    console.log(message);
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe(channel, () => {
      subscriber.quit();
      });
  }}
});
