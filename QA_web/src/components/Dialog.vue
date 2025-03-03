<template>
    <div style="display: flex;justify-content: center">
        <el-cascader
        size="large"
        :options=" pcTextArr"
        @change="toChange"
        v-model="selectedOptions">
        </el-cascader>
    </div>
</template>

<script setup>
import { useDistrictStore } from '../stores/district.js';
import {  pcTextArr } from 'element-china-area-data';
import {ref} from 'vue';
const temp = useDistrictStore();
const selectedOptions = ref(temp.district);
function toChange(){
    // console.log(selectedOptions.value);
    temp.temp_change(selectedOptions.value);
}
</script>

<style scoped>

</style>