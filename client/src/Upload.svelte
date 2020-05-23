<script>
    import {onMount} from 'svelte';
    let img;
    let long;
    let lat;
    
	onMount(() => {
        // Grab elements, create settings, etc.
        var video = document.getElementById('video');

        // Get access to the camera!
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            // Not adding `{ audio: true }` since we only want video now
            navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
                //video.src = window.URL.createObjectURL(stream);
                video.srcObject = stream;
                video.play();
            });
        }

        var canvas = document.getElementById('canvas');
        var context = canvas.getContext('2d');
        var video = document.getElementById('video');

        // Trigger photo take
        window.$('#snap').on('click', function() {
            context.drawImage(video, 0, 0, 480, 360);
            img = convertCanvasToImage(canvas);
        });
    });

    function convertCanvasToImage(canvas) {
        var image = new Image();
        image.src = canvas.toDataURL("image/png");
        return image;
    }

    function sendData() {
        navigator.geolocation.getCurrentPosition(showPosition);
    }

    function showPosition(position) {
        long = position.coords.longitude;
        lat = position.coords.latitude;
    }
</script>

<div id="upload">
    <button id="snap">Snap Photo</button>
    {#if img}
        <button id="send" on:click={sendData}>Train Model</button>
    {/if}
    <br>
    <video id="video" width="480" height="360" autoplay></video>
    <canvas id="canvas" width="480" height="360"></canvas>
</div>

<style>
    #upload {
        text-align: center;
        display: block;
    }

    button {
        margin-bottom: 20px;
    }

    #canvas {
        background-color: black;
    }
</style>