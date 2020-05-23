<script>
	import Upload from "./Upload.svelte";
	import Map from "./Map.svelte";
</script>

<main>
	<h1>Take a picture:</h1>
	<Upload/>
	<Map/>
</main>

<style>
	h1 {
		color: white;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	main {
		text-align: center;
	}
</style>