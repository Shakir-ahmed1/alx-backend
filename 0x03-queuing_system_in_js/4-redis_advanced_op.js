import redis from 'redis';


const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

client.hset('HolbertonSchools','portland', 50, redis.print);
client.hset('HolbertonSchools','Seattle', 80, redis.print);
client.hset('HolbertonSchools','New York', 20, redis.print);
client.hset('HolbertonSchools','Bogota', 20, redis.print);
client.hset('HolbertonSchools','Cali', 40, redis.print);
client.hset('HolbertonSchools','paris', 2, redis.print);
console.log(client.hgetall('HolbertonSchools', (error, data) => {
  if (error) throw error;
  console.log(data);
}));
