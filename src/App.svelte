<script>
	import Table from "./Table.svelte";
	import Menu from "./Menu.svelte";

	let rand = -1;
  function getRand() {
    fetch("http://localhost:5000/rand")
      	.then(d => d.text())
      	.then(d => (rand = d));
  }
</script>

<main>
	<h1>Your number is {rand}!</h1>
	<button on:click={getRand}>Get a random number</button>
	<Menu></Menu>
	<Table></Table>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>