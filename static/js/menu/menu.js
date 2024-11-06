const mnlateral = document.getElementById('mnlateral');
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('overlay');

        mnlateral.addEventListener('click', toggleSidebar);
        overlay.addEventListener('click', closeSidebar);

        function toggleSidebar() {
            sidebar.classList.toggle('open');
            overlay.classList.toggle('active');
            document.body.classList.toggle('sidebar-open');
        }

        function closeSidebar() {
            sidebar.classList.remove('open');
            overlay.classList.remove('active');
            document.body.classList.remove('sidebar-open');
        }