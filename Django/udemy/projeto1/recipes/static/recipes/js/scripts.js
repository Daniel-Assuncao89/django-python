function my_scope(){
    const forms = document.querySelectorAll(".delete-form");
    console.log(forms)
    
    for (const form of forms)
        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();

                const confirmed = confirm('Are you sure?');

                if (confirmed) {
                    form.submit()
                }
            })
        }
    
}

my_scope()