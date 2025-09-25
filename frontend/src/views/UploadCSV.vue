<template>
  <div class="narrow">
    <div class="card">
      <h2 class="mt-0">Upload Loan CSV</h2>
      <div class="field mb-075">
        <label class="label">CSV File</label>
        <input class="file-input" type="file" accept=".csv" @change="handleFile" />
      </div>
      <div class="field mb-1">
        <label class="label">Institution ID</label>
        <input class="input" v-model="institutionId" placeholder="Paste Institution ID here" />
      </div>
      <div class="actions">
        <button class="btn btn-success" :disabled="!file || !institutionId" @click="upload">Upload</button>
        <button class="btn btn-outline" @click="reset">Reset</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'

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
      try {
        const formData = new FormData()
        formData.append('file', this.file)
        await api.post(`/loans/import/${this.institutionId}`, formData)
        alert('CSV uploaded!')
      } catch (err) {
        console.error(err)
        alert('Upload failed')
      }
    },
    reset() {
      this.file = null
      this.institutionId = ''
    }
  }
}
</script>



