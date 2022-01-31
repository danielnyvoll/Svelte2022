<script>
	import Menu from "./Menu.svelte";
	import Table from "./Table.svelte";
	let choice = 0;
</script>

<main>
	<Menu bind:choice={choice}></Menu>
	{#if choice == 1}
	<Table></Table>
	{/if}
	{#if choice == 2}
	<h1>About Me</h1>
	{/if}
	{#if choice == 3}
	<h1>Contact</h1>
	{/if}
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