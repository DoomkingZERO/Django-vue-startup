<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>Instance: {{ instance }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      pageTrackingInterval: null,
      instance: null
    };
  },
  created() {
    this.instance = this.getNextInstanceNumber();
    this.fetchUsers();
    if (this.$route.path === '/about') {
      this.pageTracking();
      this.pageTrackingInterval = setInterval(this.pageTracking, 30000);
    }
  },
  beforeUnmount() {
    this.decreaseGlobalInstanceCounter();
    clearInterval(this.pageTrackingInterval);
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await fetch('http://localhost:8000/app/api/users/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        this.users = data.users;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async pageTracking() {
      try {
        const requestData = {
          page_id: 2,
          user_id: 1,
          instance: this.instance
        };

        const response = await fetch('http://localhost:8000/app/api/users/page', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestData)
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error:', error);
      }
    },
    getNextInstanceNumber() {
      let instance = 1;
      let globalInstanceCounter = localStorage.getItem('globalInstanceCounter');
      if (globalInstanceCounter !== null) {
        instance = parseInt(globalInstanceCounter) + 1;
      }
      localStorage.setItem('globalInstanceCounter', instance);
      return instance;
    },
    decreaseGlobalInstanceCounter() {
      localStorage.getItem('globalInstanceCounter', (value) => {
        if (value !== null) {
          const instance = parseInt(value) - 1;
          localStorage.setItem('globalInstanceCounter', instance);
        }
      });
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
