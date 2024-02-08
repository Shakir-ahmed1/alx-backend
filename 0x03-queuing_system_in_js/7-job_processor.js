import kue from 'kue';

const blacks = ['4153518780','4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacks.includes(phoneNumber)) {
    const err = `Phone number ${phoneNumber} is blacklisted`
    done(new Error(err));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // simulating sending notification with a delay
    setTimeout(()=> {
    job.complete();
    done();
    }, 500);
  }
}
const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
