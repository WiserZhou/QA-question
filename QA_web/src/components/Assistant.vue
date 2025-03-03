<template>
    <div class="wrapper">
        <div class="profileBcg">
<svg  viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="#eee" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0"><rect width="24" height="24" fill="none"></rect><path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S9 3.34 9 5H6c-1.1 0-2 .9-2 2v2c-1.66 0-3 1.34-3 3s1.34 3 3 3v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c1.66 0 3-1.34 3-3s-1.34-3-3-3zm-2 10H6V7h12v12zm-9-6c-.83 0-1.5-.67-1.5-1.5S8.17 10 9 10s1.5.67 1.5 1.5S9.83 13 9 13zm7.5-1.5c0 .83-.67 1.5-1.5 1.5s-1.5-.67-1.5-1.5.67-1.5 1.5-1.5 1.5.67 1.5 1.5zM8 15h8v2H8v-2z"></path></svg>
        </div>
        <p class="words">
            {{ props.content }}
        </p>
    </div>
</template>

<script setup>
const props = defineProps(["content"]);
</script>

<style scoped>
.wrapper {
    display: flex;
    width: 90%;
    flex-direction: row;
    /* height: 64px; */
    background-color:  #fff;
    border-radius: 1rem;
    align-items: center;
    padding: 10px;
    z-index: 0;
    /* margin: 10px; */
}
.profileBcg {
    display: flex;
    width: 2rem;
    height: 2rem;
    background-color: rgb(255, 189, 69);
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