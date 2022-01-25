<script>
	import stats from './stats.json';
    const tableHeader = Object.keys(stats[0]);
</script>

<main>
<table>
  <tr>
  {#each tableHeader as header}
    <th>{header.replace("_", " ")}</th>
	{/each}
	<th>xG90</th>
	<th>xA90</th>
  </tr>
  {#each stats as stat}
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
	<td>{Math.round(stat.xG/stat.games*100)/100}</td>
	<td>{Math.round(stat.xA/stat.games*100)/100}</td>
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