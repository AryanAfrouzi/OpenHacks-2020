<script>
    import {onMount} from 'svelte';
    let map, heatmap;
    let points;

    onMount(() => {
        points = [];
        db.collection("locations").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                for (var i = 0; i < doc.data().latitudes.length; i++) {
                    points.push({location: new google.maps.LatLng(doc.data().latitudes[i], doc.data().longitudes[i]), weight: doc.data().trash[i]});
                }
            });
            map = new google.maps.Map(document.getElementById("map-canvas"), {
                zoom: 2,
                center: {lat: 43.4643, lng: -80.5204},
                mapTypeId: 'satellite'
            });

            heatmap = new google.maps.visualization.HeatmapLayer({
                data: points,
                map: map
            });
        });
    });
        
</script>

<div id="map">
    <div id="map-canvas"></div>
</div>

<style>
    #map-canvas {
        margin: 30px 0px;
        width: 60%;
        height: 50%;
        position: absolute;
        margin-left: 20%;
    }
</style>