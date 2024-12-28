document.addEventListener('DOMContentLoaded', function() {
    const releasesContainer = document.getElementById('releases');

    fetch('https://api.github.com/repos/Aarnav-Tech/line-graph-gen/releases')
        .then(response => response.json())
        .then(data => {
            data.forEach(release => {
                const releaseItem = document.createElement('div');
                releaseItem.className = 'list-group-item';
                releaseItem.innerHTML = `
                    <div>
                        <strong>${release.name}</strong>
                        <p>${release.body}</p>
                    </div>
                    <a href="${release.html_url}" class="btn btn-primary btn-sm" target="_blank">View Release</a>
                `;
                releasesContainer.appendChild(releaseItem);
            });
        })
        .catch(error => {
            console.error('Error fetching releases:', error);
            releasesContainer.innerHTML = '<p class="text-danger">Failed to load releases.</p>';
        });
});
