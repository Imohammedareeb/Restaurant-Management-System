document.addEventListener('DOMContentLoaded', function() {
    // Form validation for reservations
    const reservationForm = document.querySelector('#reservations form');
    if (reservationForm) {
        reservationForm.addEventListener('submit', function(e) {
            const dateInput = document.getElementById('date');
            const selectedDate = new Date(dateInput.value);
            const today = new Date();
            
            // Reset previous errors
            document.querySelectorAll('.error-message').forEach(el => el.remove());
            
            // Validate date is not in the past
            if (selectedDate < today) {
                e.preventDefault();
                const errorMsg = document.createElement('div');
                errorMsg.className = 'error-message';
                errorMsg.textContent = 'Please select a future date';
                errorMsg.style.color = 'red';
                errorMsg.style.marginTop = '5px';
                dateInput.parentNode.appendChild(errorMsg);
            }
            
            // Add more validations as needed
        });
    }
    
    // Mobile menu toggle (for smaller screens)
    const mobileMenuToggle = document.createElement('button');
    mobileMenuToggle.className = 'mobile-menu-toggle';
    mobileMenuToggle.textContent = 'Menu';
    mobileMenuToggle.style.display = 'none';
    
    const nav = document.querySelector('nav');
    if (nav) {
        nav.parentNode.insertBefore(mobileMenuToggle, nav);
        
        function toggleMobileMenu() {
            if (window.innerWidth <= 768) {
                mobileMenuToggle.style.display = 'block';
                nav.style.display = 'none';
            } else {
                mobileMenuToggle.style.display = 'none';
                nav.style.display = 'block';
            }
        }
        
        mobileMenuToggle.addEventListener('click', function() {
            nav.style.display = nav.style.display === 'none' ? 'block' : 'none';
        });
        
        window.addEventListener('resize', toggleMobileMenu);
        toggleMobileMenu();
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Set current year in footer
    const yearElement = document.querySelector('footer p');
    if (yearElement) {
        const currentYear = new Date().getFullYear();
        yearElement.innerHTML = yearElement.innerHTML.replace('{{ current_year }}', currentYear);
    }
});