<template>
    <div class="demo-container">
        <div class="buttons-container">
            <div class="button-container">
                <label class="button-element">Budget</label>
                <input class="button-element" type="text" />
            </div>
            <div class="button-container">
                <label class="button-element">Max risk</label>
                <input class="button-element" type="text" />
            </div>
        </div>
        <button class="button">
            Run
        </button>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="css">
    .demo-container {
        background-color: #C9EEFF;
        width: 300px;
        height: 200px;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .button-container {
        margin: 10px;
        display: flex;
        text-align: center;
        align-items: center;
        width: 100%;
        justify-content: center;
    }
    .button-element {
        margin: 10px;
    }
    input {
        border-radius: 6px;
        border: none;
        width: 50%;
        height: 30px;
        padding: 30px;
        background-color: white;
    }
    label {
        width: 50%;
    }
    .button {
        background-color: #62CDFF;
        border: none;
        color: white;
        padding: 10px;
        border-radius: 12px;
        width: 30%;
    }
    .button:hover {
        background-color: #85d5fa;
    }
</style>