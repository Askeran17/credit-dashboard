import { mount } from '@vue/test-utils'
import InstitutionForm from '@/components/InstitutionForm.vue'
import api from '@/services/api'
import { vi, describe, it, expect, beforeEach } from 'vitest'

vi.mock('@/services/api', () => ({
  default: {
    post: vi.fn().mockResolvedValue({ data: { id: 'new-id-1' } })
  }
}))

describe('InstitutionForm.vue', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('submits form and stores id to localStorage', async () => {
    const wrapper = mount(InstitutionForm)

    await wrapper.find('input[placeholder="Name"]').setValue('Bank A')
    await wrapper.find('input[placeholder="Country"]').setValue('SE')

    await wrapper.find('form').trigger('submit.prevent')

    expect(api.post).toHaveBeenCalled()

    expect(wrapper.html()).toContain('new-id-1')

    expect(window.localStorage.getItem('institution_id')).toBe('new-id-1')
  })
})
