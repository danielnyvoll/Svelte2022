<script>
	let person;
	
	const hentPerson = async () => {
		const data = await fetch('https://fantasy.premierleague.com/api/bootstrap-static/')
		const json = await data.json()
		person = json
	}
	console.log(hentPerson());

</script>

