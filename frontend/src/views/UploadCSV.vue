<template>
  <div class="narrow">
    <div class="card">
      <h2 class="mt-0">Upload Loan CSV</h2>
      <div class="field mb-075">
        <label class="label">CSV File</label>
        <input ref="fileInput" class="file-input" type="file" accept=".csv" @change="handleFile" />
      </div>
      <div class="field mb-1">
        <label class="label">Institution ID</label>
        <input class="input" v-model="institutionId" placeholder="Paste Institution ID here" />
      </div>
      <div class="actions">
        <button class="btn btn-success" :disabled="isUploading" @click="upload">{{ isUploading ? 'Uploading…' : 'Upload' }}</button>
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
      institutionId: '',
      isUploading: false
    }
  },
  methods: {
    handleFile(e) {
      this.file = e.target.files[0]
    },
    async upload() {
      if (this.isUploading) return

      const saved = localStorage.getItem('institution_id') || ''
      const entered = (this.institutionId || '').trim()
      if (!entered || !saved || entered !== saved) {
        alert('Institution ID is required')
        return
      }
      
      if (!this.file) {
        alert('No file selected')
        return
      }

      this.isUploading = true
      try {

        const formData = new FormData()
        formData.append('file', this.file)
        await api.post(`/loans/import/${entered}`, formData)
        alert('CSV uploaded!')
        this.reset()
      } catch (err) {
        console.error(err)
        alert('Upload failed')
      } finally {
        this.isUploading = false
      }

    },
    reset() {
      this.file = null
      this.institutionId = ''
      this.isUploading = false
      if (this.$refs.fileInput) {
        this.$refs.fileInput.value = ''
      }
    }
  }
}
</script>



