// Add event listeners when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', smoothScroll);
    });

    // Form validation for the Add Book page
    const addBookForm = document.querySelector('#add-book-form');
    if (addBookForm) {
        addBookForm.addEventListener('submit', validateAddBookForm);
    }

    // Toggle book review visibility on the book details page
    const toggleReviewButton = document.querySelector('#toggle-review');
    if (toggleReviewButton) {
        toggleReviewButton.addEventListener('click', toggleReviewVisibility);
    }
});

// Smooth scrolling function
function smoothScroll(event) {
    event.preventDefault(); // Prevent default link behavior
    const targetId = this.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Validate the Add Book form
function validateAddBookForm(event) {
    const title = document.querySelector('input[name="title"]').value.trim();
    const author = document.querySelector('input[name="author"]').value.trim();
    const genre = document.querySelector('input[name="genre"]').value.trim();

    if (!title || !author || !genre) {
        event.preventDefault(); // Prevent form submission
        alert('Please fill in all required fields: Title, Author, and Genre.');
    }
}

// Toggle visibility of the book review
function toggleReviewVisibility() {
    const reviewSection = document.querySelector('#review-section');
    if (reviewSection) {
        const isVisible = reviewSection.style.display === 'block';
        reviewSection.style.display = isVisible ? 'none' : 'block';
        this.textContent = isVisible ? 'Show Review' : 'Hide Review';
    }
}