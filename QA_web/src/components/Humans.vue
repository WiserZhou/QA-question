<template>
    <div class="wrapper">
        <div class="profileBcg">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="#eee" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M10.25 13a1.25 1.25 0 11-2.5 0 1.25 1.25 0 012.5 0zM15 11.75a1.25 1.25 0 100 2.5 1.25 1.25 0 000-2.5zm7 .25c0 5.52-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2s10 4.48 10 10zM10.66 4.12C12.06 6.44 14.6 8 17.5 8c.46 0 .91-.05 1.34-.12C17.44 5.56 14.9 4 12 4c-.46 0-.91.05-1.34.12zM4.42 9.47a8.046 8.046 0 003.66-4.44 8.046 8.046 0 00-3.66 4.44zM20 12c0-.78-.12-1.53-.33-2.24-.7.15-1.42.24-2.17.24a10 10 0 01-7.76-3.69A10.016 10.016 0 014 11.86c.01.04 0 .09 0 .14 0 4.41 3.59 8 8 8s8-3.59 8-8z"></path></svg>
        </div>
        <p class="words">
            {{ prop.content }}
        </p>
    </div>
</template>

<script setup>
const prop = defineProps(["content"]);

</script>

<style scoped>
.wrapper {
    display: flex;
    width: 90%;
    /* height: 64px; */
    background-color:  rgba(240, 242, 246, 0.5);
    border-radius: 1rem;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    z-index: 0;
}
.profileBcg {
    display: flex;
    width: 2rem;
    height: 2rem;
    background-color: rgb(255, 108, 108);
    border-radius: 0.5rem;
    justify-content: center;
    align-items: center;
    align-self: flex-start;
    z-index: 10;
}
.words {
    flex: 1;
    margin-left: 1rem;
    word-wrap: break-word;
    font-family: "Source Sans Pro", sans-serif;
    margin: 0px 1rem 1rem;
    font-size: 1rem;
    font-weight: 400;
    z-index: 10;

}
</style>