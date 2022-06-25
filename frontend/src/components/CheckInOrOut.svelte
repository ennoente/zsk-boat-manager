<script lang="ts">
  import {onMount} from "svelte";
  import CheckIn from "./CheckIn.svelte";
  import CheckOut from "./CheckOut.svelte";
  import {getQueryParams} from "../utils";
  import {isBoatAlreadyCheckedIn} from "../api";

  let loading = false;
  let alreadyCheckedIn: boolean = true;

  let boatname = getQueryParams().boatname || "Unbenanntes Boot";

  onMount(() => {
    const checkIfAlreadyCheckedIn = async () => {
      console.log("awaiting...");
      alreadyCheckedIn = await isBoatAlreadyCheckedIn(boatname);
      console.log("awaited! result:", alreadyCheckedIn);
      loading = false;
    };

    console.log("calling");
    checkIfAlreadyCheckedIn();
  });
</script>

<div>
    {#await !loading}
    {:then}
        {#if alreadyCheckedIn}
            <CheckIn boatname={boatname}/>
        {:else}
            <CheckOut boatname={boatname}/>
        {/if}
    {/await}
</div>
