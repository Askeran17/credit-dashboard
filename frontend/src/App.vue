<template>
  <div class="app-root">
    <header class="app-header">
      <div class="container header-inner">
        <router-link class="brand nav-link" to="/">
          <span class="brand-icon">💳</span>
          <span class="brand-title">Credit Dashboard</span>
        </router-link>
        <nav class="nav-links">
          <router-link class="nav-link" to="/">Create</router-link>
          <router-link class="nav-link" to="/upload">Upload CSV</router-link>
          <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
          <router-link class="nav-link" to="/institutions">Institutions</router-link>
        </nav>
      </div>
    </header>

    <main class="container main-content">
      <router-view />
    </main>

    <footer class="app-footer">
      <div class="container footer-inner">
        <span>© {{ new Date().getFullYear() }} Credit Dashboard</span>
        <span class="muted">Built with Vue </span>
      </div>
    </footer>
  </div>

</template>

<script>
export default {
  computed: {
    sampleId() {
      return localStorage.getItem('institution_id') || ''
    }
  }
}
</script>







