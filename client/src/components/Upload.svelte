<script>
    import {onMount} from 'svelte';
    let img;
    let long;
    let lat;
    let numTrash;
    
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
            navigator.geolocation.getCurrentPosition(function(position) {
                long = parseFloat(position.coords.longitude.toFixed(4));
                lat = parseFloat(position.coords.latitude.toFixed(4));
            });
        });
    });

    function convertCanvasToImage(canvas) {
        var image = new Image();
        image.src = canvas.toDataURL("image/png");
        return image;
    }

    //function sendData() {
        //navigator.geolocation.getCurrentPosition(showPosition);        
    //}

    function sendData() {
        //long = parseFloat(position.coords.longitude.toFixed(4));
        //lat = parseFloat(position.coords.latitude.toFixed(4));
        numTrash = 5;
        console.log(long, lat);

        var data = db.collection("locations").doc("osV6loxQ60sNPBAY13Fv");
        let checked = false;

        data.get().then(function(doc) {
            let trashArr = doc.data().trash;
            for (var i = 0; i < doc.data().latitudes.length; i++) {
                if (long == doc.data().longitudes[i] && lat == doc.data().latitudes[i]) {
                    checked = true;
                    console.log("Data exists");
                    trashArr.splice(i, 1, numTrash);
                    data.update({
                        trash: trashArr
                    });
                    break;
                }
            }

            if (!checked) {
                console.log("Data doesn't exist");
                let trashArr = doc.data().trash;
                let longitudeArr = doc.data().longitudes;
                let latitudeArr = doc.data().latitudes;

                trashArr.push(numTrash);
                longitudeArr.push(long);
                latitudeArr.push(lat);
                db.collection("locations").doc("osV6loxQ60sNPBAY13Fv").update({
                    longitudes: longitudeArr,
                    latitudes: latitudeArr,
                    trash: trashArr
                });
            }
        });
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
    {#if numTrash != undefined}
        <p>Number of trash items: {numTrash}</p>
        <p>Refresh this page to see an updated heatmap.</p>
    {/if}
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