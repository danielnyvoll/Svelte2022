<script>
	import stats from './stats.json';
	import { onMount } from "svelte";
<<<<<<< HEAD
   const tableHeader = Object.keys(stats[0])
=======
    const tableHeader = Object.keys(stats[0]);
>>>>>>> ReadStatsToTable

	let jsonArray = []
    let rand = [];
    function getRand() {
    	fetch("./rand")
			.then(d => (d.json()))
      		.then(d => (rand = d));
  	}
	  onMount(async () => {
		getRand();
		convertJSON();
	});

	function convertJSON(){
	  jsonArray= JSON.parse(rand);
	  return jsonArray;
	}
	  
	  
<<<<<<< HEAD
    let sortedPersonData = stats;
=======
    let sortedPersonData = rand;
>>>>>>> ReadStatsToTable
	let selectedHeader = "id";
	let ascendingOrder = true;

    //Sort by numbers in the table
    const sortByNumber = (tableHeaders) =>{
		sortedPersonData = sortedPersonData.sort((obj1,obj2)=>{
			return ascendingOrder ? Number(obj1[tableHeaders]) - Number(obj2[tableHeaders])
			: Number(obj2[tableHeaders]) - Number(obj1[tableHeaders])
		});
		selectedHeader = tableHeaders;
	}
    // SORT BY STRINGs
	const sortByString = (tableHeaders) => {
		sortedPersonData = sortedPersonData.sort((obj1, obj2) => {
			if (obj1[tableHeaders] < obj2[tableHeaders]) {
					return -1;
			} else if (obj1[tableHeaders] > obj2[tableHeaders]) {
				return 1;
			}
			return 0;		
		});
		if (!ascendingOrder) {
			sortedPersonData = sortedPersonData.reverse()
		}
		selectedHeader = tableHeaders;
	}
</script>

<main>
	<table>
		<tr>
		<th>Web Name</th>
		<th>ID</th>
		<th>Minutes</th>
		<th>Goals</th>
		<th>Assist</th>
		<th>Yellow Cards</th>
		<th>Red Cards</th>
		</tr>
		{#each rand as players}
				<tr>
					{#each players as player}
					<td>{player}</td>
					{/each}
				</tr>
		{/each}
	</table>
<<<<<<< HEAD
	<button on:click={getRand}>Get players</button>
=======
>>>>>>> ReadStatsToTable

<table>
  <tr>
  {#each tableHeader as header}
    <th class:highlighted={selectedHeader === header} on:click={() => (header === "id" || header === "games" || header === "time" || header === "goals" || header === "xG" || header === "assists" || header === "xA" || header === "shots" || header === "key_passes" || header === "yellow_cards" || header === "red_cards" || header === "npg" || header === "npxG" || header === "xGChain" || header === "xGBuildup") ? sortByNumber(header) : sortByString(header)}>
				{header.replace("_", " ")}
	
	{#if header === selectedHeader}	
	<span class="order-icon" on:click={() => ascendingOrder = !ascendingOrder}>
					{@html ascendingOrder ? "&#9661;" : "&#9651;"}
				</span>{/if}</th>
	{/each}
  </tr>
  {#each sortedPersonData as stat}
  <tr>
    <td>{stat.id}</td>
    <td>{stat.player_name}</td>
    <td>{stat.games}</td>
	<td>{stat.time}</td>
    <td>{stat.goals}</td>
    <td>{Math.round(stat.xG*100)/100}</td>
	<td>{stat.assists}</td>
    <td>{Math.round(stat.xA*100)/100}</td>
    <td>{stat.shots}</td>
	<td>{stat.key_passes}</td>
    <td>{stat.yellow_cards}</td>
    <td>{stat.red_cards}</td>
	<td>{stat.position}</td>
    <td>{stat.team_title}</td>
    <td>{stat.npg}</td>
	<td>{Math.round(stat.npxG*100)/100}</td>
    <td>{Math.round(stat.xGChain*100)/100}</td>
    <td>{Math.round(stat.xGBuildup*100)/100}</td>
	</tr>
	{/each}
</table>
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
	table {
		border-spacing: 0;
		width: 100%;
		border: 1px solid #ddd;
	}
	
	th {
		text-transform: uppercase;
		cursor: pointer;
	}
	
	.order-icon {
		color: hsl(15, 100%, 25%);
	}
	
	.highlighted {
		color: hsl(15, 100%, 45%);
	}
	
	th, td {
		text-align: left;
		padding: 16px;
	}

	tr:nth-child(even) {
		background-color: #f2f2f2
	}

</style>