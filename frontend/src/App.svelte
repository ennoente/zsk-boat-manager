<script lang="ts">
  import {Route, Router} from "svelte-navigator";
  import CheckInOrOut from "./components/CheckInOrOut.svelte";
</script>

<Router>
    <main>
        <div id="main-container">
            <h2>ZSK Bootsmanager</h2>

            <Route path="/checkin">
                <CheckInOrOut/>
            </Route>

            <Route path="/checkins">
                <h3>Checkins</h3>
            </Route>
        </div>
    </main>
</Router>

<style>
    :global(html) {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: Inter var, ui-sans-serif, system-ui, sans-serif, serif;
        background-color: #f3f3f3;
    }

    :global(body) {
        width: 100vw;
        height: 100vh;
        max-width: 900px;
    }

    #main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
