<template>
  <div class="card">
    <h2 style="margin-top:0">📋 Existing Institutions</h2>
    <ul v-if="institutions.length" class="list">
      <li v-for="inst in institutions" :key="inst._id" class="list-item">
        <router-link class="nav-link" :to="`/dashboard/${inst._id}`">
          {{ inst.name }} <span class="muted">({{ inst.country }})</span>
        </router-link>
        <button class="btn btn-danger" @click="deleteInstitution(inst._id)">🗑️ Delete</button>
      </li>
    </ul>
    <p v-else class="muted">No institutions found.</p>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'InstitutionList',
  data() {
    return {
      institutions: []
    }
  },
  async mounted() {
    await this.loadInstitutions()
  },
  methods: {
    async loadInstitutions() {
      try {
        const res = await axios.get('http://localhost:8000/institutions')
        this.institutions = res.data
      } catch (err) {
        console.error('Failed to load institutions:', err)
      }
    },
    async deleteInstitution(id) {
      if (!confirm('Are you sure you want to delete this institution?')) return
      try {
        await axios.delete(`http://localhost:8000/institutions/${id}`)
        this.institutions = this.institutions.filter(inst => inst._id !== id)
      } catch (err) {
        console.error('Failed to delete institution:', err)
        alert('Deletion failed')
      }
    }
  }
}

</script>


