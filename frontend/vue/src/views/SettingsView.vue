<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        Username: {{ user.username }} | Email: {{ user.email }} | ID: {{ user.id }}
      </li>
    </ul>
  </div>
  <div class="input-group">
    <label for="userID">userID:</label>
    <input type="number" id="userID" name="userID" class="input-field" v-model="userID" placeholder="userID" required>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      userID: 1,
      pageTrackingInterval: null
    };
  },
  created() {
    this.fetchUsers();
    if (this.$route.path === '/settings') {
      this.pageTracking();
      this.pageTrackingInterval = setInterval(this.pageTracking, 30000);
    }
  },
  beforeUnmount() {
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
        this.users = data.users;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async pageTracking() {
      try {
        const requestData = {
          page_id: 1,
          user_id: this.userID,
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
