<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        Username: {{ user.username }} | Email: {{ user.email }} | ID: {{ user.id }}
      </li>
    </ul>
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
    if (this.$route.path === '/settings') {
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
        const currentTime = "2024-02-22 11:47:09";

        const requestData = {
          page_id: 1,
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
