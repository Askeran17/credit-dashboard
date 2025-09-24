<template>
  <div class="card" v-if="data">
    <h2 style="margin-top:0">Dashboard</h2>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: .75rem; margin-bottom: 1rem;">
      <div class="card">
        <div class="label">Total Loan</div>
        <div style="font-size:1.4rem; font-weight:700;">€{{ format(data.total_loan_eur) }}</div>
      </div>
      <div class="card">
        <div class="label">Invested</div>
        <div style="font-size:1.4rem; font-weight:700;">€{{ format(data.invested_eur) }} <span class="muted">({{ data.invested_percent }}%)</span></div>
      </div>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Loan No</th>
            <th>Status</th>
            <th>Amount (€)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="loan in data.loans" :key="loan.loan_id">
            <td>{{ loan.loan_no }}</td>
            <td>
              <span class="badge" :class="loan.status.toLowerCase()">{{ loan.status }}</span>
            </td>
            <td>{{ format(loan.principal_open_eur) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DashboardView',
  data() {
    return {
      data: null
    }
  },
  async mounted() {
  const id = this.$route.params.id
  if (!id) {
    this.$router.push('/')
    return
  }
  const res = await axios.get(`http://localhost:8000/dashboard/${id}`)
  this.data = res.data
},
  methods: {
    format(v) {
      try { return new Intl.NumberFormat('en-GB', { maximumFractionDigits: 2 }).format(v) } catch { return v }
    }
  }

}
</script>



