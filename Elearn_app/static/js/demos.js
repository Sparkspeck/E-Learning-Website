const popup = document.querySelector('.popup')
const inputbox = document.querySelector('.input-main')
const inputbox1 = document.querySelector('.input-main1')

const main = document.querySelector('.chatbot')
const input = document.querySelector('.input input')
const values = document.querySelector('#val')
const adds = document.querySelector('#adds')
popup.addEventListener('click', () => {

    inputbox.classList.toggle('remove')

})


document.addEventListener("DOMContentLoaded", function () {
    const tagsContainer = document.getElementById('tagsContainer');
    const searchInput = document.getElementById('searchInput');
    let tagsData = []; // Array to store tags data

    // Fetch JSON data

    fetch('/static/js/html_tags.json')
    .then(response => response.json())
        .then(data => {
            tagsData = data; // Store JSON data in tagsData array
            updateTagDetails(); // Initial update when JSON data is loaded
        })
        .catch(error => console.error('Error fetching data:', error));

    // Function to update displayed tags based on search input
    function updateTagDetails() {
        const searchTerm = searchInput.value.trim().toLowerCase();

        if (searchTerm === '') {
            tagsContainer.style.display = 'none'; // Hide container if no search term
            return;
        }

        const filteredTags = tagsData.filter(tag => tag.tag.toLowerCase().includes(searchTerm));

        if (filteredTags.length > 0) {
            tagsContainer.innerHTML = ''; // Clear previous results

            filteredTags.forEach(tag => {
                const tagElement = document.createElement('div');
                tagElement.innerHTML = `<strong>${tag.tag}</strong>: ${tag.description}<br>Example: ${tag.example}`;
                tagsContainer.appendChild(tagElement);
            });

            tagsContainer.style.display = 'block'; // Show container with results
        } else {
            tagsContainer.innerHTML = 'No tags found';
            tagsContainer.style.display = 'block'; // Show container with "No tags found" message
        }
    }

    // Add event listener to input for live searching
    searchInput.addEventListener('input', updateTagDetails);
});
