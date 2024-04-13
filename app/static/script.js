document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        alert('Form submitted!');
        // Normally, you'd handle form data here or send it to the server
        form.submit(); // This line submits the form after the alert
    });
});
