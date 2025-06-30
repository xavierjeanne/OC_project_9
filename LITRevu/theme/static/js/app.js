document.addEventListener('DOMContentLoaded', function () {

    const btn = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
  
    if (btn) {
        btn.addEventListener('click', () => {
            if (mobileMenu) {
                mobileMenu.classList.toggle('hidden');
                document.addEventListener('click', (e) => {
                  if (!btn.contains(e.target) && !mobileMenu.contains(e.target)) {
                    mobileMenu.classList.add('hidden');
                  }
                });
            }
        });
    }
    window.closeMenu = function () {
        mobileMenu.classList.add('hidden');
      };
  
  });
  