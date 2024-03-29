function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (err) {
        console.error(`Error creating job: ${err}`);
      } else {
        console.log(`Notification job created: ${job && job.id}`); // Check if job is defined before accessing its id

        job && job.on('complete', () => {
        	console.log(`Notification job ${job.id} completed`); // Check if job is defined before accessing its id
        });

        job && job.on('failed', (err) => {
        	console.error(`Notification job ${job.id} failed: ${err}`); // Check if job is defined before accessing its id
        });

        job && job.on('progress', (progress) => {
        	console.log(`Notification job ${job.id} ${progress}% complete`); // Check if job is defined before accessing its id
        });
      }
    });
  });
}

export default createPushNotificationsJobs;

