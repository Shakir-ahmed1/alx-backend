import redis from 'redis';
import {promisify} from 'util';
const client = redis.createClient()
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log('Reply: OK');
}

async function displaySchoolValue(schoolName) {
  const goten = await getAsync(schoolName);
  console.log(goten);
}
async function main() {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}
main();
