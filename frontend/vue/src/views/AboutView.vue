<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      pageTrackingInterval: null
    };
  },
  created() {
    this.fetchUsers();
    // Call pageTracking when viewing the page
    if (this.$route.path === '/about') {
      this.pageTracking();
      // Set the page tracking interval
      this.pageTrackingInterval = setInterval(this.pageTracking, 30000);
    }
  },
  beforeUnmount() {
    // Clear the interval when not viewing the page or else it keeps making requests
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
        console.log(data); // Log the response data to see its format
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
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
