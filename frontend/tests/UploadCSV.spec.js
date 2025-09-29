import { mount } from '@vue/test-utils'
import UploadCSV from '@/views/UploadCSV.vue'
import api from '@/services/api'
import { vi, describe, it, expect, beforeEach } from 'vitest'

vi.mock('@/services/api', () => ({
  default: {
    post: vi.fn().mockResolvedValue({ data: {} })
  }
}))

describe('UploadCSV.vue', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('alerts when institution id missing or not matching saved one', async () => {
    window.localStorage.setItem('institution_id', 'abc123')
    const wrapper = mount(UploadCSV)

    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {})

    await wrapper.find('button.btn-success').trigger('click')
    expect(alertSpy).toHaveBeenCalledWith('Institution ID is required')
    alertSpy.mockRestore()
  })

  it('uploads when id matches and file is present', async () => {
    window.localStorage.setItem('institution_id', 'abc123')
    const wrapper = mount(UploadCSV)

    await wrapper.find('input.input').setValue('abc123')

    const file = new File(['a,b\n1,2'], 'test.csv', { type: 'text/csv' })
    const input = wrapper.find('input[type="file"]')

    Object.defineProperty(input.element, 'files', { value: [file] })
    await input.trigger('change')

    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {})

    await wrapper.find('button.btn-success').trigger('click')

    expect(api.post).toHaveBeenCalledWith('/loans/import/abc123', expect.any(FormData))
    expect(alertSpy).toHaveBeenCalledWith('CSV uploaded!')

    alertSpy.mockRestore()
  })
})
