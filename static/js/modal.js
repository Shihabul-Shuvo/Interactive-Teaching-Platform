/**
 * Interactive Teaching Platform - Modal Handler
 * Handles displaying multimedia content in a modal overlay with Tailwind CSS
 */

const multimediaModal = document.getElementById('multimediaModal');
const modalBackdrop = document.getElementById('modalBackdrop');
const modalClose = document.getElementById('modalClose');

/**
 * Display multimedia content in modal
 * @param {Object} media - Media object from API
 */
window.displayMediaModal = function(media) {
    const titleElement = document.getElementById('multimediaTitle');
    const contentElement = document.getElementById('multimediaContent');
    
    // Set title
    titleElement.textContent = media.title || 'Content';
    
    // Render content based on media type
    let content = '';
    
    switch(media.media_type) {
        case 'text':
            content = renderTextContent(media);
            break;
        case 'image':
            content = renderImageContent(media);
            break;
        case 'audio':
            content = renderAudioContent(media);
            break;
        case 'video':
            content = renderVideoContent(media);
            break;
        case 'youtube':
            content = renderYouTubeContent(media);
            break;
        default:
            content = `<p class="text-red-500">Unknown media type: ${media.media_type}</p>`;
    }
    
    // Set content and show modal
    contentElement.innerHTML = content;
    showModal();
    
    // Track the view (analytics)
    trackMediaInteraction(media.id);
};

/**
 * Show modal with fade-in animation
 */
function showModal() {
    multimediaModal.classList.remove('hidden');
    // Lock body scroll
    document.body.style.overflow = 'hidden';
    
    // Fade in backdrop
    setTimeout(() => {
        modalBackdrop.classList.add('opacity-100');
    }, 10);
}

/**
 * Hide modal with fade-out animation
 */
function hideModal() {
    modalBackdrop.classList.remove('opacity-100');
    setTimeout(() => {
        multimediaModal.classList.add('hidden');
        document.body.style.overflow = '';
    }, 150);
}

/**
 * Render text content
 */
function renderTextContent(media) {
    let html = `
        <div class="media-container">
            <h4 class="text-lg font-semibold text-gray-900 mb-4">${media.title}</h4>
    `;
    
    if (media.description) {
        html += `<div class="text-gray-700 leading-relaxed whitespace-pre-wrap">${media.description}</div>`;
    }
    
    html += '</div>';
    return html;
}

/**
 * Render image content
 */
function renderImageContent(media) {
    let html = `
        <div class="media-container">
            <h4 class="text-lg font-semibold text-gray-900 mb-4">${media.title}</h4>
    `;
    
    if (media.file_url) {
        html += `
            <div class="image-wrapper">
                <img src="${media.file_url}" alt="${media.title}" class="w-full h-auto rounded-lg shadow-md">
            </div>
        `;
    }
    
    if (media.description) {
        html += `<p class="text-gray-700 mt-4 leading-relaxed">${media.description}</p>`;
    }
    
    html += '</div>';
    return html;
}

/**
 * Render audio content
 */
function renderAudioContent(media) {
    let html = `
        <div class="media-container">
            <h4 class="text-lg font-semibold text-gray-900 mb-4">${media.title}</h4>
    `;
    
    if (media.file_url) {
        html += `
            <div class="audio-wrapper">
                <audio class="w-full" controls>
                    <source src="${media.file_url}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
        `;
    }
    
    if (media.description) {
        html += `<p class="text-gray-700 mt-4 leading-relaxed">${media.description}</p>`;
    }
    
    html += '</div>';
    return html;
}

/**
 * Render local video content
 */
function renderVideoContent(media) {
    let html = `
        <div class="media-container">
            <h4 class="text-lg font-semibold text-gray-900 mb-4">${media.title}</h4>
    `;
    
    if (media.file_url) {
        html += `
            <div class="video-wrapper">
                <video class="w-full rounded-lg shadow-md" controls>
                    <source src="${media.file_url}" type="video/mp4">
                    Your browser does not support the video element.
                </video>
            </div>
        `;
    }
    
    if (media.description) {
        html += `<p class="text-gray-700 mt-4 leading-relaxed">${media.description}</p>`;
    }
    
    html += '</div>';
    return html;
}

/**
 * Render YouTube video content
 */
function renderYouTubeContent(media) {
    const youtubeId = extractYouTubeId(media.youtube_url);
    
    let html = `
        <div class="media-container">
            <h4 class="text-lg font-semibold text-gray-900 mb-4">${media.title}</h4>
    `;
    
    if (youtubeId) {
        html += `
            <div class="youtube-wrapper aspect-video">
                <iframe 
                    class="w-full h-full rounded-lg shadow-md" 
                    src="https://www.youtube.com/embed/${youtubeId}" 
                    title="YouTube video: ${media.title}"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
        `;
    } else {
        html += `<p class="text-red-500">Invalid YouTube URL: ${media.youtube_url}</p>`;
    }
    
    if (media.description) {
        html += `<p class="text-gray-700 mt-4 leading-relaxed">${media.description}</p>`;
    }
    
    html += '</div>';
    return html;
}

/**
 * Extract YouTube video ID from URL
 * Supports: https://www.youtube.com/watch?v=ID, https://youtu.be/ID, etc.
 */
function extractYouTubeId(url) {
    if (!url) return null;
    
    let videoId = null;
    
    // Try to extract from youtube.com/watch?v=
    const match1 = url.match(/[?&]v=([^&]+)/);
    if (match1) {
        videoId = match1[1];
    }
    
    // Try to extract from youtu.be/
    const match2 = url.match(/youtu\.be\/([^?]+)/);
    if (match2) {
        videoId = match2[1];
    }
    
    // Try to extract from youtube.com/embed/
    const match3 = url.match(/\/embed\/([^?]+)/);
    if (match3) {
        videoId = match3[1];
    }
    
    return videoId;
}

/**
 * Track multimedia interaction (analytics)
 * Sends a POST request to the tracking endpoint
 */
function trackMediaInteraction(mediaId) {
    fetch(`/api/media-items/${mediaId}/track/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            timestamp: new Date().toISOString()
        })
    })
    .catch(error => {
        // Silently fail - tracking is optional
        console.debug('Analytics tracking failed (this is okay):', error);
    });
}

/**
 * Get CSRF token from cookies
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Initialize modal event listeners
 */
document.addEventListener('DOMContentLoaded', function() {
    // Close button
    modalClose.addEventListener('click', hideModal);
    
    // Backdrop click
    modalBackdrop.addEventListener('click', hideModal);
    
    // Prevent event bubbling when clicking inside modal
    multimediaModal.addEventListener('click', function(e) {
        if (e.target === modalBackdrop || e.target === modalClose) {
            hideModal();
        }
    });
    
    // Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && !multimediaModal.classList.contains('hidden')) {
            hideModal();
        }
    });
});

