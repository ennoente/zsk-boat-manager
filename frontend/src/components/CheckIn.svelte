<script lang="ts">
  export let boatname = "";

  let trainerName = "";
  let comment = "";
  let amountRefueled: number;
</script>

<div>
    <h3>Checkin für {boatname}</h3>

    <div class="field">
        <label for="input-trainername">Name der/des Trainierenden</label>
        <input id="input-trainername" bind:value={trainerName}/>
    </div>

    <div class="field">
        <label for="input-comment">Kommentar</label>
        <textarea id="input-comment" bind:value={comment}></textarea>
    </div>

    <div class="field">
        <label for="input-amount-refueled">Wie viel wurde aufgetankt (in Kanistern, Bsp: 1.3)</label>
        <input id="input-amount-refueled" type="number" bind:value={amountRefueled}/>
    </div>
</div>

<style>
    div.field {
        width: 100%;
        margin-bottom: 2em;
    }

    div.field label {
        font-weight: bold;
        width: 100%;
        color: #f2f2f2;
    }

    div.field input, div.field textarea {
        width: 100%;
        padding: 0.5em;
        font-size: 1.2em;
        border-radius: 15px;
        box-shadow: .1em .1em #012E40;
        color: #f2f2f2;
    }

    div.field #input-comment {
        font-family: inherit;
        height: 4.6em;
    }
</style>