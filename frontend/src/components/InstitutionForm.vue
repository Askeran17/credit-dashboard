<template>
  <div class="card">
  <h2 class="mt-0">Create Credit Institution</h2>
    <form class="form-grid two" @submit.prevent="submitForm">
      <div class="field">
        <label class="label">Name</label>
        <input class="input" v-model="form.name" placeholder="Name" />
      </div>
      <div class="field">
        <label class="label">Country</label>
        <input class="input" v-model="form.country" placeholder="Country" />
      </div>
      <div class="field">
        <label class="label">Founding Year</label>
        <input class="input" v-model.number="form.founding_year" type="number" placeholder="1999" />
      </div>
      <div class="field">
        <label class="label">Total Portfolio (€)</label>
        <input class="input" v-model.number="form.total_portfolio" type="number" placeholder="1000000" />
      </div>
      <div class="field">
        <label class="label">Risk Score</label>
        <input class="input" v-model.number="form.credit_risk_score" type="number" step="0.1" placeholder="0.1" />
      </div>
      <div class="field">
        <label class="label">Product Type</label>
        <select class="select" v-model="form.product_type">
          <option disabled value="">Select Product Type</option>
          <option>Mortgage</option>
          <option>Private</option>
          <option>Business</option>
        </select>
      </div>
      <div class="field full-span">
        <label class="label">Website URL</label>
        <input class="input" v-model="form.website_url" placeholder="https://example.com" />
      </div>
      <div class="field full-span">
        <label class="label">Contacts (comma-separated)</label>
        <input class="input" v-model="form.contacts" placeholder="info@example.com, support@example.com" />
      </div>
      <div class="actions full-span">
        <button class="btn btn-primary" type="submit">Create</button>
        <button class="btn btn-outline" type="button" @click="resetForm">Reset</button>
      </div>
    </form>
    <div v-if="createdId" class="card mb-1">
      ✅ Institution created! ID: <strong>{{ createdId }}</strong>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        name: '',
        country: '',
        founding_year: 2020,
        total_portfolio: 0,
        credit_risk_score: 0,
        product_type: '',
        website_url: '',
        contacts: ''
      },
      createdId: null
    }
  },
  methods: {
    async submitForm() {
      const payload = {
        ...this.form,
        contacts: this.form.contacts.split(',').map(c => c.trim())
      }
      try {
        const res = await axios.post('http://localhost:8000/institutions', payload)
        const id = res.data.id
        this.createdId = id
        localStorage.setItem('institution_id', id)

        // Переход на дашборд
        this.$router.push(`/dashboard/${id}`)
      } catch (err) {
        console.error('Failed to create institution:', err)
      }
    },
    resetForm() {
      this.form = {
        name: '',
        country: '',
        founding_year: 2020,
        total_portfolio: 0,
        credit_risk_score: 0,
        product_type: '',
        website_url: '',
        contacts: ''
      }
    }
  }
}

</script>



