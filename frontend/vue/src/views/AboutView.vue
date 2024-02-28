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
      socket: null
    };
  },
  created() {
    this.fetchUsers();

    // Establish WebSocket connection when the component is created
    this.socket = new WebSocket('ws://localhost:8001/ws/page_tracking/');
    this.socket.onopen = () => {
    // const currentTime = new Date().toISOString();
    const message = { type: 'visit', page_id: 2, user_id: 2 };
    this.socket.send(JSON.stringify(message));
    };
  },
  unmounted() {
    if (this.socket) {
      this.socket.close();
    }
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
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
