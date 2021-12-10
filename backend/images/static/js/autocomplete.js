window.onload = () => {


    const
      searchField = document. querySelector('#main-search-q'),
      searchSuggestions = document.querySelector('#main-search-suggestions');

    function getSuggestions(value) {
      if (value == '') return [];

      const tags = [
        'anime_boys'
      ];

      const regex = new RegExp(value);
      return tags.filter((item) =>{
        if (item.match(regex)) {
          return item;
        }
      })
    }
    searchField.addEventListener('keyup', (event) => {
      const suggestions = getSuggestions(event.target.value);
      searchSuggestions.innerHTML = suggestions.map((value) => {return `<li>${value}</li>`}).join('');
    });
}
