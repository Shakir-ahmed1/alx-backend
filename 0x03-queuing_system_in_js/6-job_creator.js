const kue = require('kue');
const queue = kue.createQueue();

const job = queue.create('push_notification_code',
	{
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',

	}
).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});
job.on('failed', (errorMessage) => {
  console.log('Notification job failed');
});
job.on('complete', (result) => {
  console.log('Notification job completed');
});
