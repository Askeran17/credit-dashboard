<template>
  <div class="card">
    <h2 style="margin-top:0">Upload Loan CSV</h2>
    <div class="field" style="margin-bottom:.75rem;">
      <label class="label">CSV File</label>
      <input class="file-input" type="file" @change="handleFile" />
    </div>
    <div class="field" style="margin-bottom:1rem;">
      <label class="label">Institution ID</label>
      <input class="input" v-model="institutionId" placeholder="Paste Institution ID here" />
    </div>
    <div style="display:flex; gap:.6rem;">
      <button class="btn btn-success" @click="upload">Upload</button>
      <button class="btn btn-outline" @click="reset">Reset</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      file: null,
      institutionId: ''
    }
  },
  methods: {
    handleFile(e) {
      this.file = e.target.files[0]
    },
    async upload() {
      const formData = new FormData()
      formData.append('file', this.file)
      await axios.post(`http://localhost:8000/loans/import/${this.institutionId}`, formData)
      alert('CSV uploaded!')
    },
    reset() {
      this.file = null
      this.institutionId = ''
    }
  }
}
</script>



