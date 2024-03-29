import redis from 'redis';

const client = redis.createClient()
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  const goten = client.get(schoolName, (error, value) => {
    if (error) throw error;
    console.log(value);
  });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
