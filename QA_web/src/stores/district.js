import { defineStore } from 'pinia'

export const useDistrictStore = defineStore('district',
  {
    state: () => ({
      district: ['江西省', '吉安市'],
      temp: ['江西省', '吉安市']
    }),
    actions: {
      change() {
        this.district = this.temp;
      },
      temp_change(name) {
        this.temp = name;
      },
    },
  }
 )
