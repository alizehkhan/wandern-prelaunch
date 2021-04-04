document.addEventListener('DOMContentLoaded', () => {

  // REQUEST ACCESS BUTTONS scroll to top when clicked
  document.querySelectorAll('.request-access').forEach(button => {
    button.addEventListener('click', () => {
      // scroll up to banner
      document.querySelector('.banner').scrollIntoView({ block: 'start', behavior: 'smooth' });
      // activate & focus the email input after 0.9 secs
      setTimeout(() => document.querySelector('#email').focus(), 900);
    });
  });

  // BANNER'S DOWN ARROW scrolls down to steps
  document.querySelector(".down-arrow").addEventListener('click', () => {
    document.querySelector("#scrollStopHere").scrollIntoView({ block: 'start', behavior: 'smooth' });
  });
});
