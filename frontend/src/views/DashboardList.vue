<template>
  <div class="card">
    <h2 style="margin-top:0">📊 Dashboard</h2>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: .75rem; margin-bottom: 1rem;">
      <div class="card">
        <div class="label">Total Loan</div>
        <div style="font-size:1.4rem; font-weight:700;">€{{ format(totalLoan) }}</div>
      </div>
      <div class="card">
        <div class="label">Invested</div>
        <div style="font-size:1.4rem; font-weight:700;">€{{ format(totalInvested) }} <span class="muted">({{ investedPercent }}%)</span></div>
      </div>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Loan No</th>
            <th>Status</th>
            <th>Amount (€)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="loan in allLoans" :key="loan._id || loan.loan_id || loan.loan_no">
            <td>
              <router-link class="nav-link" :to="`/dashboard/${loan.institution_id}`">
                {{ loan.institution_name }}
              </router-link>
            </td>
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
  name: 'DashboardList',
  data() {
    return {
      allLoans: [],
      totalLoan: 0,
      totalInvested: 0,
      investedPercent: 0
    }
  },
  async mounted() {
    const res = await axios.get('http://localhost:8000/institutions')
    const institutions = res.data

    let all = []
    let total = 0
    let invested = 0

    for (const inst of institutions) {
      const dash = await axios.get(`http://localhost:8000/dashboard/${inst._id}`)
      const loansWithName = dash.data.loans.map(loan => ({
        ...loan,
        // Ensure we have the correct institution id for routing
        institution_id: inst._id,
        institution_name: inst.name
      }))
      all.push(...loansWithName)
      total += dash.data.total_loan_eur
      invested += dash.data.invested_eur
    }

    this.allLoans = all
    this.totalLoan = total
    this.totalInvested = invested
    this.investedPercent = total ? Math.round((invested / total) * 10000) / 100 : 0
  },
  methods: {
    format(v) {
      try { return new Intl.NumberFormat('en-GB', { maximumFractionDigits: 2 }).format(v) } catch { return v }
    }
  }
}
</script>



