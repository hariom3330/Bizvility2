function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function handleScroll() {
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        if (isInViewport(video)) {
            video.play();
            video.loop = true
        }
        else {
            video.pause();
        }
    });
}

window.addEventListener('scroll', handleScroll);

handleScroll();





function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


async function like_button(video_id) {
    let like_css = document.querySelector(`#thumbs_up${video_id}`);
    let dislike_css = document.querySelector(`#thumbs_down${video_id}`);

    const video_data = new FormData();
    video_data.append('video_id', video_id);
    try {
        const response = await fetch("/reels/", {
            method: 'POST',
            body: video_data,
            headers: {
                'X-CSRFToken': csrftoken,
                'X-action': 'like'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        document.querySelector(`[data-id="like${video_id}"]`).textContent = data.like;
        document.querySelector(`[data-id="dislike${video_id}"]`).textContent = data.dislike;
        // if(like_css.style.color == 'white'){
        //     like_css.style.color = 'black';
        //     dislike_css.style.color = 'white'
        // }
        // else if(like_css.style.color = 'black'){
        //     like_css.style.color = 'white';
        // }


    } catch (error) {
        console.error("Error:", error);
    }
}

async function dislike_button(video_id) {
    let like_css = document.querySelector(`#thumbs_up${video_id}`);
    let dislike_css = document.querySelector(`#thumbs_down${video_id}`);

    const video_data = new FormData();
    video_data.append('video_id', video_id);
    try {
        const response = await fetch("/reels/", {
            method: 'POST',
            body: video_data,
            headers: {
                'X-CSRFToken': csrftoken,
                'X-action': 'dislike'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        document.querySelector(`[data-id="like${video_id}"]`).textContent = data.like;
        document.querySelector(`[data-id="dislike${video_id}"]`).textContent = data.dislike;


    } catch (error) {
        console.error("Error:", error);
    }
}


async function comment_button(video_id) {
    let comment_section = document.getElementById(`comments${video_id}`).style.display
    const commentlist = document.querySelector(`.comments-list${video_id}`)
    const video_data = new FormData();
    video_data.append('video_id', video_id);
    try {
        const response = await fetch("/reels/", {
            method: 'POST',
            body: video_data,
            headers: {
                'X-CSRFToken': csrftoken,
                'X-action': 'comment'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        document.getElementById(`length${video_id}`).textContent = data.length
        commentlist.innerHTML = '';
        data.forEach((comment_data) => {
            const comment = document.createElement('div');
            comment.innerHTML = `<div class="comment">
                <img src="{{comment.user.profile}}" class="comment-avatar">
                <div class="comment-details">
                    <h3 class="comment-author">${comment_data.full_name}</h3>
                    <p class="comment-timestamp">${comment_data.timesince}</p>
                    <p class="comment-content">${comment_data.comment}</p>
                </div>
            </div>`;
            commentlist.appendChild(comment)

        })
        if (comment_section == 'none') {
            document.getElementById(`comments${video_id}`).style.display = 'block';
        }
        else {
            document.getElementById(`comments${video_id}`).style.display = 'none'
        }


    } catch (error) {
        console.error("Error:", error);
    }
}

function addComment(event,video_id){
    event.preventDefault()
    const comment = document.getElementById('comment_textarea').value;
    if (comment == '') {
      document.getElementById('emptyerror').innerHTML = '<p>Please enter a message.</p>'
      return;
    }
    const commentdata = new FormData();
    commentdata.append('comment', comment);
    commentdata.append('video_id',video_id)
    fetch('/reels/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
        'X-action': 'add_comment'
      },
      body: commentdata
    })
      .then(response => response.json())
      .then(data => {
        document.getElementById('comment_textarea').value = '';
        const commentlist = document.querySelector(`.comments-list${video_id}`)
        const comment_div = document.createElement('div')
        comment_div.innerHTML = `<div class="comment">
      <img src="${data.profile}" class="comment-avatar">
      <div class="comment-details">
        <h3 class="comment-author">${data.username}</h3>
        <p class="comment-timestamp">${data.timesince}</p>
        <p class="comment-content">${comment}</p>
      </div>
    </div>`;
    commentlist.appendChild(comment_div)
      })
      .catch(error => {
        console.error("Error: ", error);
      });
}



function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
}

function hideSidebar(){
     const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
}




const shareContainer = document.querySelector('.share-container').style.display;
function showShare() {
    const span = document.getElementById('')
    console.log(shareContainer);
    if (shareContainer == 'none') {
      document.querySelector('.share-container').style.display = 'block';
    }
    else {
      document.querySelector('.share-container').style.display = 'none';
    }
  
 
  }

function closeShare(){
    console.log("slo");
    document.querySelector('.share-container').style.display = 'none';
}