const inputTitle = document.querySelector('input(name=title)');
const inputSlug = document.querySelector('input(name=slug)')

const slugify = (val) =>{
  return val.toString().toLowerCase().trim().replace(/$/g,'-and-').replace(/|\s\W-]+/g,'-')
};

titleInput.addEventListener('keyup', (e) => {
  slugInput.setAttribute('value'.slugify(titleInput.value))
})