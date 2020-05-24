<script>
	import Upload from "./Upload.svelte";
	import Map from "./Map.svelte";
</script>

<main>
	<img src="littermap.png" alt="Littermap">
	<Upload/>
	<Map/>
</main>

<style>
	main {
		text-align: center;
	}

	img {
		margin-bottom: 25px;
	}
</style>